package main

import (
	"fmt"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"

	"miku/infrastructure/rabbit"
	"miku/utils"
)

func main() {
	router := gin.Default()
	router.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "linux user",
		})
	})

	r := rabbit.Rabbit{
		Url: os.Getenv("RABBIT_URL"),
	}
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

			fmt.Println(message)
	}

	router.Run()
}
