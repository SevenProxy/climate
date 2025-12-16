package database

import (
	"context"
	"miku/core/domain/entity"
	"miku/utils"

	"gorm.io/gorm"
)

type WeatherRepository struct {
	DB *gorm.DB
}

func (w *WeatherRepository) Create(ent *entity.Weather, ctx *context.Context) (bool, *utils.AppError) {
	err := gorm.G[entity.Weather](w.DB).Create(*ctx, ent)

	if err != nil {
		return false, &utils.AppError{
			Code: utils.CreateEntityError,
			Message: "Error ao criar entidade.",
		}
	}

	return true, &utils.AppError{
		Code: utils.NoError,
		Message: "",
	}
}
