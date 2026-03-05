"""

💡 Think of it like building a custom PC: you choose the CPU, RAM, GPU, etc.,
one by one — and only when you’re done, you “assemble” the final machine.
"""


from abc import ABC, abstractmethod


class Computer:
    """create custom pc"""

    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None
        self.storage = None
        self.os = None
        self.monitor = None

    def __str__(self):
        return (f"Computer:\n"
                f"  CPU: {self.cpu}\n"
                f"  RAM: {self.ram}\n"
                f"  GPU: {self.gpu}\n"
                f"  Storage: {self.storage}\n"
                f"  OS: {self.os}\n"
                f"  Monitor: {self.monitor}")


class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_ram(self, ram):
        pass

    @abstractmethod
    def set_gpu(self, gpu):
        pass

    @abstractmethod
    def set_storage(self, storage):
        pass

    @abstractmethod
    def set_os(self, os):
        pass

    @abstractmethod
    def set_monitor(self, monitor):
        pass

    @abstractmethod
    def get_computer(self):
        pass


class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self  # Fluent interface

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_os(self, os):
        self.computer.os = os
        return self

    def set_monitor(self, monitor):
        self.computer.monitor = monitor
        return self

    def get_computer(self):
        return self.computer


class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_gaming_pc(self):
        return (self.builder
                .set_cpu("Intel i9-14900K")
                .set_ram("64GB DDR5")
                .set_gpu("RTX 4090")
                .set_storage("2TB NVMe SSD")
                .set_os("Windows 11 Pro")
                .set_monitor("4K 144Hz")
                .get_computer())

    def build_office_pc(self):
        return (self.builder
                .set_cpu("Intel i5-13400")
                .set_ram("16GB DDR4")
                .set_gpu("Integrated")
                .set_storage("512GB SSD")
                .set_os("Windows 11 Home")
                .set_monitor("Full HD 60Hz")
                .get_computer())


if __name__ == "__main__":
    # Create builder
    builder = GamingComputerBuilder()

    # Option 1: Use Director
    director = ComputerDirector(builder)
    gaming_pc = director.build_gaming_pc()
    print(gaming_pc)

    print("\n" + "="*50 + "\n")

    # Option 2: Build manually (fluent interface)
    office_pc = (builder
                 .set_cpu("AMD Ryzen 5 5600")
                 .set_ram("32GB DDR4")
                 .set_gpu("RTX 3060")
                 .set_storage("1TB SSD")
                 .set_os("Ubuntu 24.04")
                 .set_monitor("QHD 120Hz")
                 .get_computer())

    print(office_pc)
