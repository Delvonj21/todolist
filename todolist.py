from todo import Todo


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
        lines = [f"----- {self.title} -----"]
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
        def mark_done(todo):
            todo.done = True

        self.each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False

        self.each(mark_undone)

    def all_done(self):
        return all(todo.done for todo in self._todos)

    def remove_at(self, idx):
        self._todos.pop(idx)

    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        new_list = TodoList(self.title)
        for todo in filter(callback, self._todos):
            new_list.add(todo)

        return new_list

    def find_by_title(self, title):
        found = self.select(lambda todo: todo.title == title)
        return found.todo_at(0)

    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)

    def mark_done(self, title):
        found = self.find_by_title(title)
        found.done = True


empty_todo_list = TodoList("Nothing Doing")
