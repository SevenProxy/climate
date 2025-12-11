package rabbit

import (
	"miku/utils"

	"github.com/streadway/amqp"
)

type Rabbit struct {
	url string
}

func (r *Rabbit) Connection() (*amqp.Connection, utils.AppError) {
	conn, err := amqp.Dial(r.url)

	if err != nil {
		return nil, utils.AppError{
			Code: utils.ErrorConnectionRabbit,
			Message: "Error ao fazer conexão com Rabbitmq.",
		}
	}

	return conn, utils.AppError{}
}
