def run_rag(vectorstore, query):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)

    context = "\n".join([d.page_content for d in docs])

    # simple cleaner answer extraction
    for line in context.split("\n"):
        if "CEO" in line:
            return line

    return context[:300]