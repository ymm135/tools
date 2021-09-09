package main

import (
	"log"
	//go get 下载在gopath中，下载的就是源代码!
	amqp "github.com/rabbitmq/amqp091-go"
)

func failOnError(err error, msg string) {
	if err != nil {
		log.Fatalf("%s: %s", msg, err)
	}
}

// 原文: https://github.com/rabbitmq/rabbitmq-tutorials/blob/master/go/emit_log_direct.go
func main() {
	mqUrl := "amqp://admin:admin@10.211.55.14:5672/"
	exchange := "amq.direct"
	routingKey := ""
	bodys := [...]string{"WT-CJQ-32+bond1+127.0.0.1+1590992446921+333300000016000ec6506ba986dd6000000000240001fe80000000000000e1a3c729bca00219ff0200000000000000000000000000163a000502000001008f0006c90000000104000000ff0200000000000000000001ffa00219",
		"WT-CJQ-32+bond1+127.0.0.1+1590992447173+0180c200000e000ec6506ba988cc020704000ec6506ba9040703000ec6506ba906020e11fe0900120f010300010000fe070012bb0100010100000000",
		"WT-CJQ-32+bond1+127.0.0.1+1590992447219+333300010002000ec6506ba986dd6001f1a600671101fe80000000000000e1a3c729bca00219ff0200000000000000000000000100020222022300672e7d01abc37d0008000200650001000e0001000125cfe0f8000ec6506ba90003000c3f000ec6000000000000000000270011000f4445534b544f502d414e38375244340010000e0000013700084d53465420352e30000600080011001700180027",
		"WT-CJQ-32+bond1+127.0.0.1+1590992450254+ffffffffffff000ec6506ba90800450000600c5800004011e955c0a80190c0a801ff00890089004c52b1f3dc2910000100000000000120454545464644454c464545504641434e4542454f4449444846434545444543410000200001c00c00200001000493e000066000c0a80190"}

	conn, err := amqp.Dial(mqUrl)
	failOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()

	ch, err := conn.Channel()
	failOnError(err, "Failed to open a channel")
	defer ch.Close()

	for _, value := range bodys {
		err = ch.Publish(
			exchange,
			routingKey,
			false, // mandatory
			false, // immediate
			amqp.Publishing{
				ContentType: "text/plain",
				Body:        []byte(value),
			})

		failOnError(err, "Failed to publish a message")

		log.Printf(" [x] Sent %s", value)
	}

}
