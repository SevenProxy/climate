package rabbit

import (
	"miku/utils"

	"github.com/streadway/amqp"
)

type Rabbit struct {
	Url string
}

func (r *Rabbit) Connection() (*amqp.Connection, *utils.AppError) {
	conn, err := amqp.Dial(r.Url)

	if err != nil {
		return nil, &utils.AppError{
			Code: utils.ErrorConnectionRabbit,
			Message: "Error ao fazer conexão com Rabbitmq.",
		}
	}

	return conn, &utils.AppError{
		Code: utils.NoError,
		Message: "",
	}
}

func (r *Rabbit) ChannelGet(c *amqp.Connection) (*amqp.Channel, *utils.AppError) {
	ch, err := c.Channel()

	if err != nil {
		return nil, &utils.AppError{
			Code: utils.ErrorGetChannel,
			Message: "Error ao buscar channel. Conexão inválida provavelmente.",
		}
	}

	return ch, &utils.AppError{
		Code: utils.NoError,
		Message: "",
	}
}


func (r *Rabbit) ConsumeChannel(ch *amqp.Channel, channelName string) (<-chan amqp.Delivery, *utils.AppError) {
	q, err := ch.QueueDeclare(
		channelName,
		true,
		false,
		false,
		false,
		nil,
	)

	if err != nil {
		return nil, &utils.AppError{
			Code: utils.ErrorGetChannel,
			Message: "Error ao buscar channel.",
		}
	}

	msg, err := ch.Consume(
		q.Name,
		"",
		true,
		false,
		false,
		false,
		nil,
	)

	if err != nil {
		return nil, &utils.AppError {
			Code: utils.ErrorReadMessageChannel,
			Message: "Erro ao fazer leitura do channel.",
		}
	}
	
	return msg, &utils.AppError{
		Code: utils.NoError,
		Message: "",
	}
}
