// Simple Go program to demonstrate calculation on Django server;
// Prints four triangles, calculating their hypotenuses given two sides

package main

import "C"

import (
	"math"
	"fmt"
)

// Function to find the hypotenuse given two sides of a triangle
func findHypotenuse(a, b float64) float64 {
	c_squared := a*a + b*b
	c := math.Sqrt(c_squared)
	return c
}

//export SmallTriangle
func SmallTriangle() float64 {
	return findHypotenuse(3, 4)
}

//export MediumTriangle
func MediumTriangle() float64 {
	return findHypotenuse(48, 55)
}

//export LargeTriangle
func LargeTriangle() float64 {
	return findHypotenuse(120, 209)
}

//export ExtraLargeTriangle
func ExtraLargeTriangle() float64 {
	return findHypotenuse(696, 697)
}

// Helper function to see if output is correct; not used by Django
func main() {
	one := SmallTriangle()
	fmt.Println(one)
	two := MediumTriangle()
	fmt.Println(two)
	three := LargeTriangle()
	fmt.Println(three)
	four := ExtraLargeTriangle()
	fmt.Println(four)
}