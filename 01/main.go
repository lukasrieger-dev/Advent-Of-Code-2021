package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	increase_count := 0
	current_depth := 99999999

	sonar, err := readLines("input.txt")
	if err != nil {
		fmt.Println("[ERROR] Failed to read input file.")
	}
	// first part simple diffs
	for _, measurement := range sonar {
		m := stringToInt(measurement)
		if current_depth-m < 0 {
			increase_count++
		}
		current_depth = m
	}
	fmt.Println("Simple depth increases:", increase_count)

	// second part using sliding windows
	increase_count = 0
	for idx, measurement := range sonar {
		if idx+3 < len(sonar) {
			if measurement < sonar[idx+3] {
				increase_count++
			}
		}
	}
	fmt.Println("Sliding windows depth increases:", increase_count)
}

func stringToInt(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		fmt.Println(err)
		os.Exit(2)
	}
	return i
}

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}
