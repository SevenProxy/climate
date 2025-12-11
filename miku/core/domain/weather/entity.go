package weather

type Weather struct {
	Time		int `json:"time_r"`
	Temperature float64 `json:"temperature"`
	Humitity	[]int `json:"humitity"`
	WindSpeed	float64 `json:"wind_speed"`
}
