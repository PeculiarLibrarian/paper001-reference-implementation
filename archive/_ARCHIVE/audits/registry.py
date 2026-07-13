from peculiarlibrary.audits.compiler_audit import CompilerAudit
from peculiarlibrary.audits.constitution_audit import ConstitutionAudit
from peculiarlibrary.audits.domain_audit import DomainAudit
from peculiarlibrary.audits.kernel_audit import KernelAudit

AUDITS = [
    CompilerAudit(),
    ConstitutionAudit(),
    DomainAudit(),
    KernelAudit()
]
