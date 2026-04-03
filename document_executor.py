#!/usr/bin/env python3
import argparse

from agent_factory import agent_factory

def doc_agent_executor(filepath : str, model: str = "gpt-4o-mini", chunk_length: int = 3):
    
    doc_agent = agent_factory("doc_agent", model)

    context = "Following the doc to setup some env on local host using passowrd 'root'. Have not done any thing till now. this is just the beginning."

    with open(filepath, 'r') as file:
        lines = file.readlines()

    # Remove any empty lines or lines with just whitespace
    lines = [line.strip() for line in lines if line.strip()]

    agent_iteration = 0
    # Iterate over the lines, chunk_length at a time
    for i in range(0, chunk_length, chunk_length):
        chunk = lines[i:i+chunk_length]
        # Join the lines into a single string variable
        instruction_block = '\n'.join(chunk)
        agent_iteration += 1
        print(f"============ started agent iteration {agent_iteration} ============")
        input = "Here is context of previous chunks execution till now:: \n" + context + "\nHere is the current chunk of the document:: \n" + instruction_block
        result = doc_agent.invoke({"messages": [{"role": "assistant", "content": input}]})
        print(result)
        context = result['message']
        print(f"\n\n============ new context after iteration {agent_iteration} ============")
        print(context)


def document_executor():
    parser = argparse.ArgumentParser(prog="docu")
    subparsers = parser.add_subparsers(dest="command")

    execute_parser = subparsers.add_parser("execute")
    execute_parser.add_argument(
        "--filepath",
        required=True,
        help="Path to the document",
    )
    execute_parser.add_argument(
        "--model",
        default=None,
        help="Model name to use. By default 'gpt-4o-mini' will be used",
    )
    execute_parser.add_argument(
        "--chunk_length",
        type=int,
        default=None,
        help="Optional chunk length (integer)",
    )

    args = parser.parse_args()

    if args.command == "execute":
        doc_agent_executor(args.filepath, args.model, args.chunk_length)
    else:
        parser.print_help()
