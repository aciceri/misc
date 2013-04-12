.data
	msg: .string "Hello world!\n"
	len: .int .-msg
.text
	.globl main

main:
	movl $4, %eax
	movl $1, %ebx
	movl $msg, %ecx
	movl len, %edx
	int $0x80

	xorl %eax, %eax
	int $0x80
