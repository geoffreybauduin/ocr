package main

import (
	"image"
	"image/png"
	"image/draw"
	"io/ioutil"
	"log"
	"bytes"
	"strconv"
)

func main () {
	var letters = []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "2", "2", "2", "2", "2", "3", "3", "3", "3", "3", "4", "4", "4", "4", "4", "5", "5", "5", "5", "5", "6", "6", "6", "6", "6", "7", "7", "7", "7", "7", "8", "8", "8", "8", "8", "9", "9", "9", "9", "9"}
	data, err := ioutil.ReadFile("./all.png")
	if err != nil {
		log.Println(err)
	} else {
		img, err := png.Decode(bytes.NewReader(data))
		if err != nil {
			log.Println(err)
		} else {
			i := 0
			for i < 84 {
				j := int64(0)
				for j < 52 {
					im := image.NewRGBA(image.Rect(0, 0, 20, 20))
					draw.Draw(im, im.Bounds(), img, image.Point{int(j * 20), int(i * 20)}, draw.Src)
					buf := new(bytes.Buffer)
					png.Encode(buf, im)
					letters = letters
					ioutil.WriteFile("./tests/" + letters[i] + "_" + strconv.FormatInt(j, 10) + ".png", buf.Bytes(), 0777)
					j++
				}
				i++	
			}
		}
	}
}