from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import pandas as pd

data = pd.read_csv("combined_data.csv")

# print(data.head())

message = data['text']
labels = data['label']

# message = [
#     "Congratulations! You’ve won a $1000 gift card. Click here to claim now!",
#     "Dear user, your account will be suspended unless you verify your password immediately.",
#     "Limited offer! Buy one get one free. Hurry before stock runs out!",
#     "Hi, I’m a prince from Nigeria. I need your help transferring $5 million. You’ll get a reward!",
#     "You have an overdue bill. Pay now to avoid penalties.",
#     "Earn money fast working from home. No experience needed!",
#     "Your package delivery failed. Click this link to reschedule.",
#     "Get your miracle weight loss pills today!",
#     "Final reminder: your PayPal account has been locked. Log in here.",
#     "This is not spam. Please open the attached document for urgent details.",
#     "Hey there! Just checking in about tomorrow’s meeting.",
#     "Can we reschedule our lunch to next week?",
#     "Here’s the report you asked for. Let me know if it looks good.",
#     "Reminder: Project submission due on Friday.",
#     "Let’s catch up this weekend!"
# ]
# labels = [
#     "spam","spam","spam","spam","spam","spam","spam","spam","spam","spam","not_spam","not_spam", "not_spam", "not_spam", "not_spam"
# ]

vectorizer = CountVectorizer()
msg = vectorizer.fit_transform(message)

train_data ,test_data, train_label,test_labels=train_test_split(msg,labels,test_size=.3)

model = MultinomialNB()
model.fit(train_data,train_label)


result = model.predict(test_data)

print(result)

accuracy = accuracy_score(test_labels,result)
confusionMatrix = confusion_matrix(test_labels,result)
classificationReport =classification_report(test_labels,result)
print(accuracy)
print(confusionMatrix)
print(classificationReport)


