package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func (r rot13Reader) Read(s []byte) (int, error) {
	byread, err := r.r.Read(s)
	for i := range s[:byread] {
		n := s[i]
		if 'A' <= n && n <= 'Z' {
			n += 13
			if n > 'Z' {
				n -= 26
			}
		} else if 'a' <= n && n <= 'z' {
			n += 13
			if n > 'z' {
				n -= 26
			}
		} else {
			continue
		}
		s[i] = n
	}
	return byread, err
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
