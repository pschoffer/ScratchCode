package main

import (
	"fmt"
	"reflect"
)

var (
	course = "da"
	module = 3.6
)

func main()  {
	name := "Pavel"
	fmt.Println("Hello from", name, reflect.TypeOf(course), module )
}