# Emulating the cpu behavior for Chip-8

class cpu ():
    def __init__(self):
        # Defining Memory (4KB)
        self.memory = [0] * 4096 
        # Defining Cpu Registers (8b)
        self.V = [0] * 16
        # Special Reigsters (16b)
        self.I = 0

        #  Stack Pointers etc.
        self.pc = 0x200   # Program starts at memory address 0x200
        self.stack = [0] * 16 # Chip-8 stack allows 16 nested levels "slots"
        self.sp = 0 # Stack pointer
        
        # Timers 
        self.delay_timer = 0
        self.sound_timer = 0

        # IN/OUT
        self.display = [0] * (64 * 32)
        self.keypad = [0] * 16

        # Class methods
        def cycle(self):
            # 1. fetch the Op-codes
            opcode = self.memory[self.pc] << 8 | self.memory[self.pc + 1]

            self.pc += 2
            
            # Decode the op-codes
            category = (opcode & 0xF000) >> 12 # Defines the category section of the Opcode.
            x = (opcode & 0x0F00) >> 8 # Defines the target register
            y = (opcode & 0x00F0) >> 4
            kk = (opcode & 0x00FF)
            n = (opcode & 0x000F)
            nnn = (opcode & 0x0FFF)

            if category == 0x1: # Jumps to an address (NNN)
                self.pc = nnn
            
            if category == 0x6: # Set register to value (kk)
                self.V[x] = kk
            
            if category == 0x7: # Add value (kk) to register 
                self.V[x] = (self.V[x] + kk) & 0xFF

            

            
        


