package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	num1, num2 := 0, 0
	twice_return := false
	return func() int {
		if num2 == 0 {
			num2 = 1
			return num1
		} else if twice_return == false {
			twice_return = true
			return 1
		} else {
			num1, num2 = num2, num1 + num2
			return num2
		}
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
