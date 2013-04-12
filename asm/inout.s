.data
	str: .string ""
	len: .int 0
.text
	.globl main

main:
	movl $3, %eax
	movl $1, %ebx
	movl $str, %ecx
	movl $100, %edx
	int $0x80

	movl $4, %eax
	movl $1, %ebx
	movl $str, %ecx
	movl $100, %edx
	int $0x80

	xorl %eax, %eax
	int $0x80
