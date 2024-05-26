import torch
from nemo.collections.asr.models import ASRModel
from nemo.core import typecheck

typecheck.set_typecheck_enabled(enabled=False)

model = ASRModel.from_pretrained(model_name="stt_en_conformer_ctc_small", trainer=None)

model.preprocessor = torch.compile(model.preprocessor)
model.encoder = torch.compile(model.encoder)

data = model.encoder.input_example()
# print(data)
data = [
    torch.randn(1, 5 * model.cfg.sample_rate, device=model.device),
    torch.tensor([5 * model.cfg.sample_rate], dtype=torch.int64, device=model.device),
]
out = model(*data)