# Auto-generated
#from app.site.models import *

from typing import List, Dict, Any, Optional

import os
import json

from .models import *

PROJECT_TIMESTAMPS: List[ProjectTimestamp] = []

DB_TIMESTAMPS: List[DBTimestamp] = []

PROJECTS: List[Project] = []

FUNCTIONS: List[Function] = []

CONSTRUCTORS: List[Function] = []

BLOCKERS: List[BranchBlocker] = []

BUILD_STATUS: List[BuildStatus] = []

PROJECT_DEBUG_DATA: List[DebugStatus] = []

ALL_HEADER_FILES: List[Dict[str, Any]] = []


def get_projects() -> List[Project]:
    return PROJECTS


def get_functions() -> List[Function]:
    return FUNCTIONS


def get_constructors() -> List[Function]:
    return CONSTRUCTORS


def get_blockers() -> List[BranchBlocker]:
    return BLOCKERS


def get_build_status() -> List[BuildStatus]:
    return BUILD_STATUS


def get_debug_data() -> List[DebugStatus]:
    return PROJECT_DEBUG_DATA


def get_project_debug_report(project: str) -> Optional[DebugStatus]:
    debug_report_path = os.path.join(
        os.path.dirname(__file__),
        f"../static/assets/db/db-projects/{project}/debug_report.json")
    print(f"getting path: {debug_report_path}")
    if not os.path.isfile(debug_report_path):
        print("Failed")
        return None

    with open(debug_report_path, 'r') as f:
        debug_report = json.load(f)

    debug_model = DebugStatus(
        project_name=project,
        all_files_in_project=debug_report.get('all_files_in_project', []),
        all_functions_in_project=debug_report.get('all_functions_in_project',
                                                  []),
        all_global_variables=debug_report.get('all_global_variables,', []),
        all_types=debug_report.get('all_types', []))
    return debug_model


def get_project_branch_blockers(project: str) -> List[BranchBlocker]:
    branch_blockers_path = os.path.join(
        os.path.dirname(__file__),
        f"../static/assets/db/db-projects/{project}/branch_blockers.json")
    print(f"getting path: {branch_blockers_path}")
    if not os.path.isfile(branch_blockers_path):
        print("Failed")
        return []

    with open(branch_blockers_path, 'r') as f:
        branch_report = json.load(f)

    branch_models = list()
    for json_bb in branch_report:
        branch_models.append(
            BranchBlocker(project_name=json_bb.get('project', ''),
                          function_name=json_bb.get('function_name', ''),
                          unique_blocked_coverage=json_bb.get(
                              'blocked_runtime_coverage'),
                          source_file=json_bb.get('source_file'),
                          blocked_unique_functions=json_bb.get(
                              'blocked_unique_functions'),
                          src_linenumber=json_bb.get('linenumber')))
    return branch_models
