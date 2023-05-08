# 汇编OJ

## 出题意图

shellcode入门，学会使用x64汇编/系统调用

## 解法

本题唯一的难点就是字符串的处理，因为开了pie，所以你用gpt直接生成的答案应该是有的问题的。

解决方法有很多，比如把字符串的内容压到栈里（x64汇编不能直接push 64位立即数进栈）

这里给出另一种解法，用PC来相对寻址

```assembly
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
```

