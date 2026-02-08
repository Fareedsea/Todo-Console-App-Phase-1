---
description: "Task list for console todo app implementation"
---

# Tasks: Console Todo App (COMPLETED)

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification did not explicitly request test tasks, so they are not included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 [P] Create project directory structure (src/, tests/, src/models/, src/services/, src/cli/, src/lib/)
- [x] T002 [P] Create main.py entry point in src/lib/main.py
- [x] T003 Create README.md with project overview

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Foundational tasks for the console todo app:

- [x] T004 [P] Create Task model in src/models/task.py with id, title, description, status, created_at fields
- [x] T005 [P] Create TaskRepository class in src/services/task_repository.py with in-memory storage
- [x] T006 Create ConsoleUI class in src/cli/console_ui.py with basic menu structure
- [x] T007 Implement error handling utilities for validation and user-friendly messages

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to create and view todo tasks with titles and descriptions in the console application

**Independent Test**: Can be fully tested by adding tasks and viewing the task list to verify they appear correctly with appropriate status and metadata.

### Implementation for User Story 1

- [x] T008 [P] [US1] Implement Task model validation methods (title not empty, status enum) in src/models/task.py
- [x] T009 [US1] Implement create_task method in src/services/task_repository.py with auto-increment ID
- [x] T010 [US1] Implement get_all_tasks method in src/services/task_repository.py
- [x] T011 [US1] Implement add_task functionality in src/cli/console_ui.py menu option
- [x] T012 [US1] Implement view_tasks functionality in src/cli/console_ui.py menu option
- [x] T013 [US1] Update main.py to integrate Task model, TaskRepository, and ConsoleUI for US1 features
- [x] T014 [US1] Add title validation (not empty) to task creation in src/models/task.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update and Delete Tasks (Priority: P2)

**Goal**: Enable users to modify or remove existing tasks by updating title/description or deleting entirely

**Independent Test**: Can be fully tested by updating and deleting tasks by ID, then verifying the changes persist correctly in the task list.

### Implementation for User Story 2

- [x] T015 [P] [US2] Implement get_task_by_id method in src/services/task_repository.py
- [x] T016 [P] [US2] Implement update_task method in src/services/task_repository.py
- [x] T017 [US2] Implement delete_task method in src/services/task_repository.py
- [x] T018 [US2] Implement update_task functionality in src/cli/console_ui.py menu option
- [x] T019 [US2] Implement delete_task functionality in src/cli/console_ui.py menu option
- [x] T020 [US2] Update main.py to integrate US2 features with existing functionality
- [x] T021 [US2] Add task ID validation in src/services/task_repository.py for update/delete operations

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Completion (Priority: P3)

**Goal**: Enable users to mark tasks as complete or incomplete to track their progress by toggling status

**Independent Test**: Can be fully tested by toggling task status by ID, then verifying the status changes correctly in the task list.

### Implementation for User Story 3

- [x] T022 [P] [US3] Implement toggle_task_status method in src/services/task_repository.py
- [x] T023 [US3] Implement mark_task_completion functionality in src/cli/console_ui.py menu option
- [x] T024 [US3] Update main.py to integrate US3 features with existing functionality
- [x] T025 [US3] Add status toggle validation in src/models/task.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T026 [P] Add comprehensive error handling for invalid menu choices in src/cli/console_ui.py
- [x] T027 [P] Add input validation for all user inputs across all modules
- [x] T028 Add graceful exit functionality to main.py
- [x] T029 Add timestamp formatting utilities for created_at field
- [x] T030 Run quickstart.md validation and update main.py as needed

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before CLI features
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence