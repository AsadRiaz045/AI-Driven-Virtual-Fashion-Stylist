👗 AI Fashion Stylist & Size Recommender
📌 Project Overview
The AI Fashion Stylist is a computer vision-based solution designed to solve the common "Size Mismatch" problem in online shopping. By scanning the user's body in real-time, the system provides accurate measurements and recommends the perfect clothing size based on specific brand charts (e.g., Junaid Jamshed & Outfitters).

🚀 Key Features
Real-time Body Measurement: Uses the MediaPipe BlazePose model to track 33 body landmarks and calculate Chest and Waist dimensions.

Brand-Specific Recommendations: Integrated official size charts for popular brands to ensure a tailored fit.

Instant Analysis: Optimized for speed with a fixed 0.045 calibration ratio, providing results without lag.

Style Assistance: Analyzes skin tone and suggests the best-suited color palettes for the user.

🛠️ Tech Stack
Language: Python

Computer Vision: OpenCV & MediaPipe

Deployment: Streamlit (Web Interface)

Mathematics: NumPy (for Euclidean distance calculations and geometry)

📐 How It Works
Pose Detection: The MediaPipe engine identifies 33 key landmarks on the human body.

Distance Calculation: The system calculates the pixel distance between specific landmarks (e.g., shoulder-to-shoulder) using the Euclidean distance formula.

Calibration: A fixed ratio of 0.045 inches per pixel converts digital measurements into real-world inches.

Size Mapping: The calculated measurements are compared against the size_config.py database to find the best fit (S, M, L, XL).

💻 Installation & Usage
Clone the repository:
git clone https:(https://github.com/AsadRiaz045/AI-Driven-Virtual-Fashion-Stylist)
Install dependencies:
pip install -r requirements.txt
Run the application:
streamlit run app.py
