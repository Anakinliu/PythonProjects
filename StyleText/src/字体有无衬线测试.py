# target_name = "sha"  # png 有serif
target_name = "sha2"  # png 无serif
style_name = "sakura"
has_Serif = False
if has_Serif:
    cmd = f"""--text_name ../data/oth/words/dis/{target_name}_dis.png --scale -1 --scale_step 0.05 --structure_model ../save/{style_name}-GS.ckpt --texture_model ../save/{style_name}-GT.ckpt --result_dir ../output/{style_name}-{target_name}-WITH-serif --name {style_name}-{target_name} --gpu """
else:
    cmd = f"""--text_name ../data/oth/words/dis/{target_name}_dis.png --scale -1 --scale_step 0.05 --structure_model ../save/{style_name}-GS.ckpt --texture_model ../save/{style_name}-GT.ckpt --result_dir ../output/{style_name}-{target_name}-NO-serif --name {style_name}-{target_name} --gpu """

print(cmd)