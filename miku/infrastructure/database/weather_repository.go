package database

import (
	"context"
	"miku/core/domain/weather"
	"miku/utils"

	"gorm.io/gorm"
)

type WeatherRepository struct {
	db *gorm.DB
}

func (w *WeatherRepository) Create(entity *weather.Weather, ctx *context.Context) (bool, utils.AppError) {
	err := gorm.G[weather.Weather](w.db).Create(*ctx, entity)

	if err != nil {
		return false, utils.AppError{
			Code: utils.CreateEntityError,
			Message: "Error ao criar entidade.",
		}
	}

	return true, utils.AppError{}
}
