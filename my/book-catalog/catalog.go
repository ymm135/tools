package main

import (
	"container/list"
	"fmt"
	"io/ioutil"
	"os"
	"regexp"
	"strings"
)

func main() {
	// 读取输入文件
	currPath, _ := os.Getwd()

	// 输入文件路径, 使用os.Stdin vscode命令行无法交互输入
	file, err := os.Open(currPath + "/my/book-catalog/input.file")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	contents, err := ioutil.ReadAll(file)
	strs := string(contents)
	lines := strings.Split(strs, "\n")
	results := list.New()

	// 解析数据
	for _, line := range lines {
		// 去除小节
		matched, _ := regexp.MatchString(`\d.\d.\d`, line)
		if matched {
			continue
		}

		// 然后通过空格分组，去除最后一个
		contents := strings.Split(line, " ")
		contents = contents[0 : len(contents)-1]
		line = strings.Join(contents, " ")
		results.PushBack(line)
	}

	for i := results.Front(); i != nil; i = i.Next() {
		fmt.Println(i.Value)
	}

}
