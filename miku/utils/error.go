package utils

type erroCode int

const (
	ErrorDatabase erroCode = iota
	CreateEntityError
	ErrorNotFound
	ErrTimeout

	ErrorConnectionRabbit
	ErrorGetChannel
	ErrorReadMessageChannel
)

type AppError struct {
	Code	erroCode
	Message	string
}

func (a *AppError) Error() string {
	return a.Message
}
