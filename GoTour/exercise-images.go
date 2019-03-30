package main

import (
	"image"
	"image/color"

	"golang.org/x/tour/pic"
)

type Image struct {
}

func (i Image) ColorModel() color.Model {
	return color.RGBAModel
}

func (i Image) Bounds() image.Rectangle {
	return image.Rect(0, 0, 255, 255)
}

func (i Image) At(x, y int) color.Color {
	return color.RGBA{uint8(x+x), uint8(y/100), uint8(x), uint8(y*x)}
}

func main() {
	m := Image{}
	pic.ShowImage(m)
}
