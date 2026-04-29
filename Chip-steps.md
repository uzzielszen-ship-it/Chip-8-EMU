
# CHIP - 8 Learning Manual

This will be a general collection of the steps current and future of the chip-8 emu and their implementations throughout the project process.

First and foremost the refences for the Project.

1) Chip 8 technical manuals -> http://devernay.free.fr/hacks/chip8/C8TECH10.HTM

2) https://wojlin.github.io/js-chip8/docs.html 


----------------------------------------------------------------------------------------------------

## CPU and MEMORY functions

All the discussion of specific memory architecture and stack functions etc are made in refernce to the Chip-8 Technical Manual.

Chip-8's language is able to access up to 4KB of Random Acess Memory, denoted in hexadecimal notation from 0x000 to 0x0FFF (4095). Most if not all Chip-8 Programs begin on the memory address 0x200 because the original interpreter is located from 0x000 to 0x1FF and should not be manipulated.

As mentioned beforehand, Chip-8 has 4KB of usuable memory for programs, howver it should be known that the "stack" is seperate from this 4KB. The stack utilizes 16 "slots" each able to contain 16bit memory addresses which are used to read of instructions.

Memory is stored in 8 bit sections, same goes for the cpu registers with the exeption of a special register "I". Chip-8 Opcode is 16bits or 2 bytes long, and must be read in two segments in the cpu. 

    Which leads to: opcodes = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
The first section of the memory address is shifted back 8 spaces to account and make room for the second segment which is needed to complete the Opcode.

## Understanding Opcodes

Opcodes are comprised of 4 "nibbles" or 4 sections of 4 bytes. Opcodes are also written in Hexadecimal notation, take for example: 0x8120 .
 1) The first nibble 8 is refered to as the "Category" this defines the instruction type which in this case is arithmetic.

 2) The second nibble "1" is the "x", this represents the index of the first memory register (V1).

 3) The third nibble "2" is the "y", this represents the index of the second memory register (V2).

 4) The fourth nibble "0" is the "n", this represents the "Sub-code" which would tell you wich math problem to preform, for example 0x8120 means to set V1 = V2, whereas 0x8124 means to add V1 and V2 and the output is saved to the target register V1.

Also an important distinction to make it that the category of the Opcode tells the cpu how to read the rest of it. Earlier we looked at the Opcode 0x8120, category 8 (Arithmetic) tells the cpu to set V1 represented by (1) to the value in v2 represented by (2). 
Now if for example we had an Opcode with a different category such as 0x1125, the Cpu would read this as follows.
    
        0x1125 -> Jump to (1) -> Memory address 125. 
The opcode is in the format 0x1NNN instead of 0x8XYN.

## Important Categories
Some categories to take note of are the D, F, and A categories. These bridge the gap between the game's logic and the virtual hardware.

Category A: Responsible for pointing the I register to a specific memory address. This tells the CPU where to look for data before it performs an action.

Category D: The Draw category, responsible for putting sprites on the screen. It uses XOR logic, meaning it can both draw and "erase" pixels, which is how games detect collisions.

Category F: A collection of essential instructions that handle everything from timers and keyboard input to math. Notably, it contains instructions like Fx29 that calculate the exact memory location of built-in font sprites.

### More on 0xF33
    The reasoning behind why we may need to break up a number such as 125 into segments is because Chip-8 lacks a print function. This means that it doesnt or would not be able to understand the number 125 as is, we must break it up into numbers 1, 2, and 5 which each have their sprites for being put on the screen located in memory.
