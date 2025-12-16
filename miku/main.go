package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"

	"miku/infrastructure/rabbit"
	"miku/infrastructure/database"
	"miku/core/domain/usecase"
	"miku/utils"
)

func main() {
	if err := godotenv.Load(); err != nil {
		log.Fatal("Error ao carregar .ENV")
	}

	router := gin.Default()
	router.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "linux user",
		})
	})
	
	db := database.Init("host=localhost user=miku password=flamengo dbname=climate port=5432 sslmode=disable TimeZone=America/Sao_Paulo")
	connection, err := db.Connection()

	if err.Code == utils.ErrorDatabase {
		fmt.Println(err.Message)
		return
	}
	
	repo := database.WeatherRepository{
		DB: connection,
	}

	r := rabbit.NewRabbit(os.Getenv("RABBIT_URL"))
	conn, err := r.Connection()

	switch err.Code {
		case utils.ErrorConnectionRabbit:
			fmt.Println(err.Error())

		case utils.NoError:
			ch, err := r.ChannelGet(conn)
			if err.Code == utils.ErrorGetChannel {
				fmt.Println(err.Error())
				return
			}
			
			message, err := r.ConsumeChannel(ch, "climate_channel")
			
			if err.Code == utils.ErrorReadMessageChannel {
				fmt.Println(err.Error())
				return
			}

			entities, err := r.ReadMessage(message)
			
			if err.Code == utils.ErrorReadMessage {
				return
			}

			weather := usecase.WeatherUseCase{
				R: &repo,
			}

			for ind := range entities {
				weather.CraeteWeather(&entities[ind])
			}
	}

	router.Run()
}
