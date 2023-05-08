.global _start
.intel_syntax noprefix
_start:
    lea rdi,[rip + flagtext]
    mov rsi,0
    mov rdx,0
    mov rax,2
    syscall
    mov rdi,rax
    sub	rsp,60
    mov rsi,rsp
    mov rdx,60
    mov rax,0
    syscall
    mov rdi,2
    mov rsi,rsp
    mov rdx,rax
    mov rax,1
    syscall
    mov rax,60
    mov rdx,0x0
    syscall
flagtext:
	.ascii "./flag"
