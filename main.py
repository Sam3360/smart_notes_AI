import os
from embedder import get_embedding
from database import load_index, save_index, add_note, search
from ai import ask_llm
from rich import print
from rich.panel import Panel

NOTES_DIR = "notes"


# 📝 Add Note
def add_note_ui():
    print(Panel("Enter your note below", title="📝 Add Note"))

    text = input("> ").strip()
    if not text:
        print("[red]❌ Empty note not allowed[/red]")
        return

    emb = get_embedding(text)

    index, meta = load_index(len(emb))
    add_note(index, meta, emb, text)
    save_index(index, meta)

    print("[green]✅ Note added successfully[/green]")


# 🔍 Search Notes
def search_ui():
    print(Panel("Search your notes", title="🔍 Search"))

    q = input("> ").strip()
    if not q:
        print("[red]❌ Empty query[/red]")
        return

    emb = get_embedding(q)

    index, meta = load_index(len(emb))

    if len(meta) == 0:
        print("[yellow]⚠️ No notes found. Add some first.[/yellow]")
        return

    results = search(index, meta, emb)

    print("\n[bold cyan]Top Matches:[/bold cyan]")

    if not results:
        print("[red]❌ No relevant notes found[/red]")
        return

    for text, score in results:
        print(f"[green]- {text}[/green] [dim](score: {round(score, 2)})[/dim]")


# 💬 Chat Mode (RAG)
def chat_ui():
    print(Panel("Ask questions from your notes", title="💬 Chat Mode"))

    q = input("> ").strip()
    if not q:
        print("[red]❌ Empty query[/red]")
        return

    emb = get_embedding(q)

    index, meta = load_index(len(emb))

    if len(meta) == 0:
        print("[yellow]⚠️ No notes available[/yellow]")
        return

    results = search(index, meta, emb)

    if not results:
        print("[red]❌ No relevant context found[/red]")
        return

    # Build context
    context = "\n".join([r[0] for r in results])

    print("\n[yellow]🧠 Thinking...[/yellow]\n")

    try:
        answer = ask_llm(context, q)
    except Exception as e:
        print("[red]❌ LLM not running. Start Ollama first.[/red]")
        return

    print(Panel(answer, title="🤖 AI Answer"))


# 📊 Stats (NEW — makes it feel pro)
def stats_ui():
    index, meta = load_index(384)  # embedding size for MiniLM

    print(Panel("Database Stats", title="📊 Info"))

    print(f"[cyan]Total Notes:[/cyan] {len(meta)}")
    print(f"[cyan]Index Size:[/cyan] {index.ntotal}")


# 🎮 Main Menu (THIS is your menu — already included)
def menu():
    while True:
        print(Panel(
            "[bold cyan]Smart Notes AI[/bold cyan]\n"
            "1. Add Note\n"
            "2. Search Notes\n"
            "3. Chat with Notes\n"
            "4. Stats\n"
            "5. Exit",
            title="🚀 Menu"
        ))

        choice = input("> ").strip()

        if choice == "1":
            add_note_ui()
        elif choice == "2":
            search_ui()
        elif choice == "3":
            chat_ui()
        elif choice == "4":
            stats_ui()
        elif choice == "5":
            print("[bold green]👋 Goodbye[/bold green]")
            break
        else:
            print("[red]❌ Invalid choice[/red]")


# 🚀 Entry point
if __name__ == "__main__":
    os.makedirs(NOTES_DIR, exist_ok=True)
    menu()