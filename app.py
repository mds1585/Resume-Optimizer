import openai

class ResumeOptimizerWithChatGPT:
    def __init__(self, resume, job_description, api_key):
        self.resume = resume
        self.job_description = job_description
        openai.api_key = api_key

    def call_chatgpt(self, prompt):
        """
        Makes a call to ChatGPT with a given prompt.
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a professional resume optimizer."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

    def analyze_job_description(self):
        """
        Step 1: Use ChatGPT to analyze the job description and extract key requirements.
        """
        prompt = f"Analyze the following job description and list key skills, experiences, and qualifications in bullet points:\n\n{self.job_description}"
        return self.call_chatgpt(prompt)

    def analyze_resume(self):
        """
        Step 2: Use ChatGPT to analyze the resume and extract highlighted skills, experiences, and qualifications.
        """
        prompt = f"Analyze the following resume and list key skills, experiences, and qualifications in bullet points:\n\n{self.resume}"
        return self.call_chatgpt(prompt)

    def identify_gaps(self, job_requirements, resume_features):
        """
        Step 3: Use ChatGPT to compare the job description with the resume and identify gaps.
        """
        prompt = f"Compare the following job requirements:\n\n{job_requirements}\n\nWith the following resume features:\n\n{resume_features}\n\nIdentify gaps and suggest additions to better align the resume with the job description."
        return self.call_chatgpt(prompt)

    def rewrite_resume(self, suggestions):
        """
        Step 4: Use ChatGPT to rewrite the resume based on identified gaps and suggestions.
        """
        prompt = f"Using the following suggestions, rewrite the resume to better align with the job description:\n\nSuggestions:\n{suggestions}\n\nOriginal Resume:\n{self.resume}"
        return self.call_chatgpt(prompt)

    def review_updated_resume(self, updated_resume):
        """
        Step 5: Use ChatGPT to review the updated resume and provide final recommendations.
        """
        prompt = f"Review the following updated resume for clarity, conciseness, and impact. Provide final recommendations:\n\n{updated_resume}"
        return self.call_chatgpt(prompt)

    def optimize(self):
        """
        Execute the full optimization process with ChatGPT.
        """
        job_requirements = self.analyze_job_description()
        resume_features = self.analyze_resume()
        gaps = self.identify_gaps(job_requirements, resume_features)
        updated_resume = self.rewrite_resume(gaps)
        final_feedback = self.review_updated_resume(updated_resume)
        return updated_resume, final_feedback


# Example usage:
resume_content = "Your current resume content here"
job_description_content = "The job description content here"
api_key = "your-openai-api-key-here"

optimizer = ResumeOptimizerWithChatGPT(resume_content, job_description_content, api_key)
final_resume, recommendations = optimizer.optimize()

print("Optimized Resume:")
print(final_resume)
print("\nFinal Recommendations:")
print(recommendations)
