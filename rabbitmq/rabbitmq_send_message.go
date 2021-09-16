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
	// mqUrl := "amqp://admin:admin@10.25.10.201:5672/"
	exchange := "amq.direct"
	routingKey := ""
	// 采集器序列号+工作网卡+IP+时间戳+数据包（16进制）
	bodys := [...]string{
		//COTP
		"WT-CJQ-32+bond1+127.0.0.1+1590992451254+000ec4cca311001b1beb834f08004500003e049400003c06f7a3c0a800eac0a800480066ef4aa855510dd53680d050180800062f00000300001611d00001443100c0010ac1020100c2020102",
		//S7COMM
		"WT-CJQ-32+bond1+127.0.0.1+1590992452258+001b1beb834f000ec4cca3110800450000414138400080060000c0a80048c0a800eaef4a0066d53680d0a85551235018fada82b600000300001902f08032010000390200080000f0000001000101e0",
		//TCP
		"WT-CJQ-32+bond1+127.0.0.1+1590992453259+000ec4cca311001b1beb834f080045000028049300003c06f7bac0a800eac0a800480066ef4aa855510dd53680d050100800e6360000000000000000",
	}

	conn, err := amqp.Dial(mqUrl)
	failOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()

	ch, err := conn.Channel()
	failOnError(err, "Failed to open a channel")
	defer ch.Close()

	for i := 0; i <= 10000; i++{
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

}
