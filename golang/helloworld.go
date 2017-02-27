package main

import "fmt"
// import "reflect"

// type Header map[string][]string

func main() {
	fmt.Println("hello world")
	var a *string
	b := "hello pointer"
	a = &b
	fmt.Println(*a)


	// h := make(Header)
	// fmt.Println(reflect.TypeOf(h))
	// fmt.Println(h)
}
