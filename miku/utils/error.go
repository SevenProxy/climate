package utils

type erroCode int

const (
	ErrorDatabase erroCode = iota
	CreateEntityError
	ErrorNotFound
	ErrTimeout
)

type AppError struct {
	Code	erroCode
	Message	string
}

func (a *AppError) Error() string {
	return a.Message
}
