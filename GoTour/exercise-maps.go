package main

import (
	"strings"

	"golang.org/x/tour/wc"
)

func WordCount(s string) map[string]int {
	word_count := make(map[string]int)
	for _, word := range strings.Fields(s) {
		word_count[word]++
	}
	return word_count
}

func main() {
	wc.Test(WordCount)
}
