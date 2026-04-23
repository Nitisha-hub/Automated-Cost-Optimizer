# 💸 AWS Automated Cost Optimizer

## 🎯 Project Objective
Automatically reduce AWS cost by stopping unused EC2 instances.

## 🧰 Services Used
- AWS Lambda
- Amazon EC2
- Amazon CloudWatch

## ⚙️ How It Works
1. CloudWatch triggers Lambda daily
2. Lambda checks EC2 instances
3. Stops running/idle instances
4. Saves cost automatically

## 📊 Architecture
![Architecture](architecture-diagram.png)

## 🧪 Steps to Reproduce
1. Launch EC2 instance
2. Deploy Lambda function
3. Create CloudWatch trigger
4. Test automation

## 📸 Screenshots
(Add your screenshots here)

## 💡 Future Improvements
- Add CPU-based stopping logic
- Email notification using SNS
- Tag-based filtering

## 👩‍💻 Author
Nitisha Mali
