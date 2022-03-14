import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md

master = mt.TcpMaster("127.0.0.1", 502)
master.set_timeout(5.0)


def data_collect():
    data_sam = master.execute(slave=3, function_code=md.READ_HOLDING_REGISTERS, starting_address=0, quantity_of_x=10,
                              output_value=100)
    return data_sam


if __name__ == '__main__':
    print(data_collect())
