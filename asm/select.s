.bss
	var: .string ""
.data
	msg: .string "Inserisci 0 o 1: "
	msg_len: .int .-msg
.text
	.globl main

main:
	movl $4, %eax
	movl $1, %ebx
	movl $msg, %ecx
	movl msg_len, %edx
	int $0x80

	movl $3, %eax
	movl $1, %ebx
	movl $var, %ecx
	movl $2, %edx
	int $0x80

	xorl %eax, %eax
	int $0x80
