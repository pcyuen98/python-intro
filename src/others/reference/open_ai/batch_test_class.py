import json

class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def to_dict(self):
        return {"role": self.role, "content": self.content}

    def __repr__(self):
        return f"Message(role={self.role}, content={self.content})"


class Request:
    def __init__(self, custom_id: str, method: str, url: str, model: str, messages: list, max_tokens: int):
        self.custom_id = custom_id
        self.method = method
        self.url = url
        self.body = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens
        }

    def to_dict(self):
        return {
            "custom_id": self.custom_id,
            "method": self.method,
            "url": self.url,
            "body": self.body
        }

    def __repr__(self):
        return (f"Request(custom_id={self.custom_id}, method={self.method}, "
                f"url={self.url}, body={self.body})")


class GPTJson:
    @staticmethod
    def create(request_no, msg):
        messages = [Message(role="user", content=msg)]
    
        request = Request(
            custom_id="request-" + request_no,
            method="POST",
            url="/v1/chat/completions",
            model="gpt-3.5-turbo-0125",
            messages=[message.to_dict() for message in messages],
            max_tokens=1000
        )

        print(request)
    
        # Convert to JSON
        json_request = json.dumps(request.to_dict())
        return json_request


# Example usage
if __name__ == "__main__":
    data = [
    ["Raja Petra has passed away in the UK, as reported by the New Straits Times. For more information and extensive coverage, readers can access the full story on Google News. Is this a positive, not politic related and important news? Answer yes or no only."],
    ["Raja Petra has passed away in the UK, as reported by the New Straits Times. For more information and extensive coverage, readers can access the full story on Google News. explain this in psychology way of life view"]
]
    
    temp_file = open("_temp.jsonl", "w", encoding="utf-8")
    
        
    for row_index, row in enumerate(data):          
        result = GPTJson.create(str(row_index + 1), row)
        print("result -->", result)
        temp_file.write(result + "\n")

    temp_file.close()