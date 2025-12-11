package usecase

import (
	"context"

	"miku/infrastructure/database"
	"miku/utils"
	"miku/core/domain/entity"
)

type WeatherUseCase struct {
	r *database.WeatherRepository
}

func (w *WeatherUseCase) CraeteWeather(e *entity.Weather) (bool, utils.AppError) {
	ctx := context.Background()
	return  w.r.Create(e, &ctx)
}
