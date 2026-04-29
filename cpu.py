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

        # Font
        font = [
    0xF0, 0x90, 0x90, 0x90, 0xF0, # 0
    0x20, 0x60, 0x20, 0x20, 0x70, # 1
    0xF0, 0x10, 0xF0, 0x80, 0xF0, # 2
    0xF0, 0x10, 0xF0, 0x10, 0xF0, # 3
    0x90, 0x90, 0xF0, 0x10, 0x10, # 4
    0xF0, 0x80, 0xF0, 0x10, 0xF0, # 5
    0xF0, 0x80, 0xF0, 0x90, 0xF0, # 6
    0xF0, 0x10, 0x20, 0x40, 0x40, # 7
    0xF0, 0x90, 0xF0, 0x90, 0xF0, # 8
    0xF0, 0x90, 0xF0, 0x10, 0xF0, # 9
    0xF0, 0x90, 0xF0, 0x90, 0x90, # A
    0xE0, 0x90, 0xE0, 0x90, 0xE0, # B
    0xF0, 0x80, 0x80, 0x80, 0xF0, # C
    0xE0, 0x90, 0x90, 0x90, 0xE0, # D
    0xF0, 0x80, 0xF0, 0x80, 0xF0, # E
    0xF0, 0x80, 0xF0, 0x80, 0x80  # F
    ]
        for i in range(len(font)):
            self.memory[i] = font[i]

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
            
        elif category == 0x6: # Set register to value (kk)
            self.V[x] = kk
            
        elif category == 0x7: # Add value (kk) to register 
            self.V[x] = (self.V[x] + kk) & 0xFF
            
        elif category == 0xA:
            self.I = nnn
        
        elif category == 0x2:
            # Call function
            self.stack[self.sp] = self.pc # save the current position in memory to the stack
            self.sp += 1 # increment the stack by 1
            self.pc = nnn # move our position in memory to a memory adress nnn.
        
        elif category == 0x0:
            if kk == 0xEE: # Return function
                if self.sp > 0:
                    self.sp -= 1
                    self.pc = self.stack[self.sp]
        
        elif category == 0xF: # Misc category
            if kk == 0x07:
                self.V[x] = self.delay_timer
            elif kk == 0x15:
                self.delay_timer = self.V[x]
            elif kk == 0x0A:
                key_pressed = False
                for k in range(16):     # sadly i wont write descriptions for each instruction...
                    if self.keypad[k] == 1:
                        self.V[x] = k
                        key_pressed = True
                        break
                if key_pressed == False:
                    self.pc -=2
            elif kk == 0x18:
                self.sound_timer = self.V[x]
            elif kk == 0x1E:
                self.I = (self.I + self.V[x])
            elif kk == 0x29:
                self.I = self.V[x] * 5
            elif kk == 0x33:
                value = self.V[x]
                self.memory[self.I] = value // 100
                self.memory[self.I + 1] = (value // 10) % 10
                self.memory[self.I + 2] = (value) % 10
            elif kk == 0x55:
                for i in range(x + 1):
                    self.memory[self.I + i] = self.V[i]
            elif kk == 0x65:
                for i in range(x+1):
                    self.V[i] = self.memory[self.I + i]
        
        # 





        
            
            

            

            
        


