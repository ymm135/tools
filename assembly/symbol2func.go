package main

import (
	"container/list"
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
	"strings"
)

/**
通过c++filt把汇编语言中的符号表转化为函数签名
*/
func main() {

	// 读取输入文件
	currPath, _ := os.Getwd()

	// 输入文件路径, 使用os.Stdin vscode命令行无法交互输入
	file, err := os.Open(currPath + "/input.file")
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
		if strings.Contains(line, "<_Z") {
			start := strings.Index(line, "<_Z")
			end := strings.LastIndex(line, ">")

			funcSymbol := line[start+1 : end]
			// 执行c++filt 命令
			cmd := exec.Command("/usr/bin/c++filt", funcSymbol)
			out, _ := cmd.CombinedOutput()
			funcName := string(out)

			line = line[:start] + funcName
		}
		results.PushBack(line)
	}

	for i := results.Front(); i != nil; i = i.Next() {
		fmt.Println(i.Value)
	}
}
