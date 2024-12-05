# Define a custom Batch class
class BatchGPTDummy:
    def __init__(self):
        self.id = None
        self.output_file_id = None

    def set_value(self, id, output_file_id):
        self.id = id
        self.output_file_id = output_file_id
        return self

# Create an instance of BatchGPTDummy and set its values
b = BatchGPTDummy().set_value(777, "1234")

# Access the attributes of the BatchGPTDummy object
print(b.output_file_id)