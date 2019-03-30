package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := x/2
	i := 0
	for ; math.Abs((z*z - x) / (2 * z)) > .000000000000001 ; i++ {
		z -= (z*z - x) / (2 * z)
	}
	fmt.Println("# of iterations:", i)
	return z
}

func main() {
	fmt.Printf("Mine: %v StdLib: %v", Sqrt(3), math.Sqrt(3))
}
