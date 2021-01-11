#!/usr/bin/env python

print("# groupby-polars.py", flush=True)

import os
import gc
import timeit
import pypolars as pl
from pypolars.lazy import col

exec(open("./_helpers/helpers.py").read())

ver = pl.__version__
git = "unknown"
task = "groupby"
solution = "polars"
fun = ".groupby"
cache = "TRUE"
on_disk = "FALSE"

data_name = os.environ["SRC_DATANAME"]
src_grp = os.path.join("data", data_name + ".csv")
print("loading dataset %s" % data_name, flush=True)

x = pl.read_csv(
    src_grp,
    dtype={
        "id4": pl.Int32,
        "id5": pl.Int32,
        "id6": pl.Int32,
        "v1": pl.Int32,
        "v2": pl.Int32,
        "v3": pl.Float64,
    },
)
x["id1"] = x["id1"].cast(pl.Categorical)
x["id2"] = x["id2"].cast(pl.Categorical)
x["id3"] = x["id3"].cast(pl.Categorical)

in_rows = x.shape[0]
x = x.lazy()

print(len(x.collect()), flush=True)

task_init = timeit.default_timer()
print("grouping...", flush=True)

question = "sum v1 by id1"  # q1
gc.collect()
t_start = timeit.default_timer()
q = x.groupby("id1").agg(pl.sum("v1"))
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = [ans["v1_sum"].sum()]
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=1,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
del ans
gc.collect()
t_start = timeit.default_timer()
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = [ans["v1_sum"].sum()]
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=2,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
print(ans.head(3), flush=True)
print(ans.tail(3), flush=True)
del ans

question = "sum v1 by id1:id2"  # q2
gc.collect()
t_start = timeit.default_timer()
q = x.groupby(["id1", "id2"]).agg([pl.sum("v1")])
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = [ans["v1_sum"].sum()]
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=1,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
del ans
gc.collect()
t_start = timeit.default_timer()
q = x.groupby(["id1", "id2"]).agg([pl.sum("v1")])
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = [ans["v1_sum"].sum()]
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=2,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
print(ans.head(3), flush=True)
print(ans.tail(3), flush=True)
del ans

question = "sum v1 mean v3 by id3"  # q3
gc.collect()
t_start = timeit.default_timer()
q = x.groupby("id3").agg([pl.sum("v1"), pl.mean("v3")])
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = list(
    ans.lazy().select([pl.sum("v1_sum"), pl.sum("v3_mean")]).collect().to_numpy()
)
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=1,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
del ans
gc.collect()
t_start = timeit.default_timer()
q = x.groupby("id3").agg([pl.sum("v1"), pl.mean("v3")])
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = list(
    ans.lazy().select([pl.sum("v1_sum"), pl.sum("v3_mean")]).collect().to_numpy()
)
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=2,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
print(ans.head(3), flush=True)
print(ans.tail(3), flush=True)
del ans

question = "mean v1:v3 by id4"  # q4
gc.collect()
t_start = timeit.default_timer()
q = x.groupby("id4").agg([pl.mean("v1"), pl.mean("v2"), pl.mean("v3")])
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = list(
    ans.lazy()
    .select([pl.sum("v1_mean"), pl.sum("v2_mean"), pl.sum("v3_mean")])
    .collect()
    .to_numpy()
)
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=1,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
del ans
gc.collect()
t_start = timeit.default_timer()
q = x.groupby("id4").agg([pl.mean("v1"), pl.mean("v2"), pl.mean("v3")])
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = list(
    ans.lazy()
    .select([pl.sum("v1_mean"), pl.sum("v2_mean"), pl.sum("v3_mean")])
    .collect()
    .to_numpy()
)
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=2,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
print(ans.head(3), flush=True)
print(ans.tail(3), flush=True)
del ans

question = "sum v1:v3 by id6"  # q5
gc.collect()
t_start = timeit.default_timer()
q = x.groupby("id6").agg([pl.sum("v1"), pl.sum("v2"), pl.sum("v3")])
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = list(
    ans.lazy()
    .select([pl.sum("v1_sum"), pl.sum("v3_sum"), pl.sum("v3_sum")])
    .collect()
    .to_numpy()
)
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=1,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
del ans
gc.collect()
t_start = timeit.default_timer()
q = x.groupby("id6").agg([pl.sum("v1"), pl.sum("v2"), pl.sum("v3")])
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = list(
    ans.lazy()
    .select([pl.sum("v1_sum"), pl.sum("v3_sum"), pl.sum("v3_sum")])
    .collect()
    .to_numpy()
)
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=2,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
print(ans.head(3), flush=True)
print(ans.tail(3), flush=True)
del ans

question = "median v3 sd v3 by id4 id5"  # q6
gc.collect()
t_start = timeit.default_timer()
q = x.groupby(["id4", "id5"]).agg(
    [pl.median("v3").alias("v3_median"), pl.std("v3").alias("v3_std")]
)
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
print(ans)
chk = list(
    ans.lazy().select([pl.sum("v3_median"), pl.sum("v3_std")]).collect().to_numpy()
)
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=1,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
del ans
gc.collect()
t_start = timeit.default_timer()
q = x.groupby(["id4", "id5"]).agg(
    [pl.median("v3").alias("v3_median"), pl.std("v3").alias("v3_std")]
)
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = list(
    ans.lazy().select([pl.sum("v3_median"), pl.sum("v3_std")]).collect().to_numpy()
)
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=2,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
print(ans.head(3), flush=True)
print(ans.tail(3), flush=True)
del ans

question = "max v1 - min v2 by id3"  # q7
gc.collect()
t_start = timeit.default_timer()

q = (
    x.groupby("id3")
    .agg([col("v1").max().alias("v1"), col("v2").min().alias("v2")])
    .select(["id3", (col("v1") - col("v2")).alias("range_v1_v2")])
)
ans = q.collect()

print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = [ans["range_v1_v2"].sum()]
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=1,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
del ans
gc.collect()
t_start = timeit.default_timer()

q = (
    x.groupby("id3")
    .agg([col("v1").max().alias("v1"), col("v2").min().alias("v2")])
    .select(["id3", (col("v1") - col("v2")).alias("range_v1_v2")])
)

ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = [ans["range_v1_v2"].sum()]
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=2,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
print(ans.head(3), flush=True)
print(ans.tail(3), flush=True)
del ans

question = "largest two v3 by id6"  # q8
gc.collect()
t_start = timeit.default_timer()
q = (
    x.drop_nulls(["v3"])
    .sort("v3", reverse=True)
    .groupby("id6")
    .agg([col("v3").head(2).alias("v3_top_2")])
    .explode("v3_top_2")
)
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = [ans["v3_top_2"].sum()]
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=1,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
del ans
gc.collect()
t_start = timeit.default_timer()

q = (
    x.drop_nulls(["v3"])
    .sort("v3", reverse=True)
    .groupby("id6")
    .agg([col("v3").head(2).alias("v3_top_2")])
    .explode("v3_top_2")
)

ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = [ans["v3_top_2"].sum()]
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=2,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
print(ans.head(3), flush=True)
print(ans.tail(3), flush=True)
del ans

question = "regression v1 v2 by id2 id4"  # q9
gc.collect()
t_start = timeit.default_timer()

q = (
    x.drop_nulls(["v1", "v2"])
    .groupby(["id2", "id4"])
    .agg([pl.pearson_corr("v1", "v2").alias("r2")])
    .with_column(col("r2") ** 2)
)

ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = [ans["r2"].sum()]
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=1,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
del ans
gc.collect()
t_start = timeit.default_timer()
q = (
    x.drop_nulls(["v1", "v2"])
    .groupby(["id2", "id4"])
    .agg([pl.pearson_corr("v1", "v2").alias("r2")])
    .with_column(col("r2") ** 2)
)

ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = [ans["r2"].sum()]
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=2,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
print(ans.head(3), flush=True)
print(ans.tail(3), flush=True)
del ans

question = "sum v3 count by id1:id6"  # q10
gc.collect()
t_start = timeit.default_timer()
q = x.groupby(["id1", "id2", "id3", "id4", "id5", "id6"]).agg(
    [pl.sum("v3").alias("v3"), pl.count("v1").alias("v1")]
)
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = list(ans.lazy().select([pl.sum("v3"), pl.sum("v1")]).collect().to_numpy())
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=1,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
del ans
gc.collect()
t_start = timeit.default_timer()
q = x.groupby(["id1", "id2", "id3", "id4", "id5", "id6"]).agg(
    [pl.sum("v3").alias("v3"), pl.count("v1").alias("v1")]
)
ans = q.collect()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = list(ans.lazy().select([pl.sum("v3"), pl.sum("v1")]).collect().to_numpy())
chkt = timeit.default_timer() - t_start
write_log(
    task=task,
    data=data_name,
    in_rows=in_rows,
    question=question,
    out_rows=ans.shape[0],
    out_cols=ans.shape[1],
    solution=solution,
    version=ver,
    git=git,
    fun=fun,
    run=2,
    time_sec=t,
    mem_gb=m,
    cache=cache,
    chk=make_chk(chk),
    chk_time_sec=chkt,
    on_disk=on_disk,
)
print(ans.head(3), flush=True)
print(ans.tail(3), flush=True)
del ans

print(
    "grouping finished, took %0.fs" % (timeit.default_timer() - task_init), flush=True
)

exit(0)
