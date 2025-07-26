class Todo:
    IS_DONE = "X"
    NOT_DONE = " "

    def __init__(self, title):
        self._title = title
        self._done = False

    @property
    def title(self):
        return self._title

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, done):
        self._done = done 

    def __str__(self):
        if self.done:
            marker = Todo.IS_DONE
        else:
            marker = Todo.NOT_DONE

        return f"[{marker}] {self.title}"
    
    def __eq__(self, other):
        if isinstance(other, Todo):
            return self.title == other.title and self.done == other.done
        
        return NotImplemented

class TodoList:

    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title
    
    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Can only add Todo objects")
        
        self._todos.append(todo)

    def __str__(self):
        lines = [f"---- {self.title} ----"]
        lines += [str(todo) for todo in self._todos]
        return "\n".join(lines)
    
    def __len__(self):
        return len(self._todos)
    
    def first(self):
        return self._todos[0]
    
    def last(self):
        return self._todos[-1]
    
    def to_list(self):
        return self._todos.copy()
    
    def todo_at(self, idx):
        return self._todos[idx]
    
    def mark_done_at(self, idx):
        self.todo_at(idx).done = True

    def mark_undone_at(self, idx):
        self.todo_at(idx).done = False

    def mark_all_done(self):
        for todo in self._todos:
            todo.done = True

    def mark_all_undone(self):
        for todo in self._todos:
            todo.done = False

    def all_done(self):
        return all(todo.done for todo in self._todos)
    
    def remove_at(self, idx):
        self._todos.pop(idx)


