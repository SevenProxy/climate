package database

import (
	"gorm.io/gorm"
	"gorm.io/driver/postgres"
	"miku/utils"
)

type Database struct {
	dsn string
}

func Init(url string) *Database {
	return &Database{
		dsn: url,
	}
}

func (d *Database) Connection() (*gorm.DB, utils.AppError) {
	//dsn := "host=localhost user=miku password=flamengo port=5432 sslmode=disable"
	db, err := gorm.Open(postgres.Open(d.dsn), &gorm.Config{})

	if err != nil {
		return nil, utils.AppError {
			Code: utils.ErrorDatabase,
			Message: "Conexão com banco de dados não foi efetuada",
		}
	}
	
	return db, utils.AppError{}
}
