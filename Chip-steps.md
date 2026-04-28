

This will be a general collection of the steps current and future of the chip-8 emu and their implementations throughout the project process.

First and foremost the refences for the Project.

1) Chip 8 technical manuals -> http://devernay.free.fr/hacks/chip8/C8TECH10.HTM

2) https://wojlin.github.io/js-chip8/docs.html 


----------------------------------------------------------------------------------------------------

CPU and MEMORY functions

All the discussion of specific memory architecture and stack functions etc are made in refernce to the Chip-8 Technical Manual.

Chip-8's language is able to access up to 4KB of Random Acess Memory, denoted in hexadecimal notation from 0x000 to 0x0FFF (4095). Most if not all Chip-8 Programs begin on the memory address 0x200 because the original interpreter is located from 0x000 to 0x1FF and should not be manipulated.

As mentioned beforehand, Chip-8 has 4KB of usuable memory for programs, howver it should be known that the "stack" is seperate from this 4KB. The stack utilizes 16 "slots" each able to contain 16bit memory addresses which are used to read of instructions.

Memory is stored in 8 bit sections, same goes for the cpu registers with the exeption of special registers like BC and other "Combined registers". Chip-8 Opcode is 16bits or 2 bytes long, and must be read in two segments in the cpu. 

    Which leads to: opcodes = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
The first section of the memory address is shifted back 8 spaces to account and make room for the second segment which is needed to complete the Opcode.
