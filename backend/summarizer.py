import ollama
import os

client = ollama.Client(
    host=os.environ.get("OLLAMA_HOST", "http://localhost:11434")
)

def chunk_transcript(transcript, max_chars=3000):
    chunks = []
    current = []
    current_len = 0

    for seg in transcript:
        text = f"[{seg['start']:.2f}] {seg['text']}"
        if current_len + len(text) > max_chars and current:
            chunks.append(current)
            current = []
            current_len = 0
        current.append(text)
        current_len += len(text)

    if current:
        chunks.append(current)

    return chunks

def summarize_chunk(chunk_text, chunk_num, total):
    prompt = f"""
This is part {chunk_num} of {total} of a video transcript.
Summarize the key points from this section only.

Transcript:
{chunk_text}
"""
    response = client.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.message.content

def generate_notes(transcript):
    chunks = chunk_transcript(transcript)
    total = len(chunks)

    if total == 1:
        text = "\n".join(
            f"[{x['start']:.2f}] {x['text']}" for x in transcript
        )
        prompt = f"""
Analyze this transcript and generate:

1. Executive Summary
2. Key Topics
3. Important Timestamps
4. Action Items
5. Study Notes

Transcript:
{text}
"""
        response = client.chat(
            model="llama3.2:1b",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.message.content
        if not result:
            raise Exception("LLaMA returned empty response")
        return result

    else:
        summaries = []
        for i, chunk in enumerate(chunks):
            chunk_text = "\n".join(chunk)
            summary = summarize_chunk(chunk_text, i+1, total)
            summaries.append(f"--- Part {i+1} ---\n{summary}")

        combined = "\n\n".join(summaries)

        final_prompt = f"""
Below are summaries from different parts of a long video.
Combine them into one cohesive set of notes with:

1. Executive Summary
2. Key Topics
3. Important Timestamps
4. Action Items
5. Study Notes

Summaries:
{combined}
"""
        response = client.chat(
            model="llama3.2:1b",
            messages=[{"role": "user", "content": final_prompt}]
        )
        result = response.message.content
        if not result:
            raise Exception("LLaMA returned empty response")
        return result