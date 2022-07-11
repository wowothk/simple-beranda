# import os
# import pandas as pd

from connect_database import run_query, open_ssh_tunnel, mysql_connect, mysql_disconnect


class Data:

    open_ssh_tunnel()
    mysql_connect()

    @staticmethod
    def get_data_keaktifan():
        keaktifan = """
            SELECT kota, kecamatan, kelurahan,
                (
                IF(bamuskal > 0,1,0) + IF(covid > 0,1,0) + IF(dukuh > 0,1,0) + IF(kepen_agama > 0,1,0) +
                IF(kepen_dusun > 0,1,0) + IF(kepen_kawin > 0,1,0) + IF(kepen_kerja > 0,1,0) + IF(kepen_pend > 0,1,0) +
                IF(kepen_tumbuh > 0,1,0) + IF(kepen_usia > 0,1,0) + IF(kesej_kerja > 0,1,0) + IF(kesej_penduduk > 0,1,0) +
                IF(keu_pendapatan > 0,1,0) + IF(keu_pengeluaran > 0,1,0) + IF(layanan > 0,1,0) + IF(lembaga > 0,1,0) +
                IF(pegawai > 0,1,0) + IF(sarana_ibadah > 0,1,0) + IF(sarana_kebersihan > 0,1,0) + IF(sarana_kesehatan > 0,1,0) +
                IF(sarana_pendidikan > 0,1,0) + IF(sarana_sanitasi > 0,1,0) + IF(sarana_transportasi > 0,1,0) + IF(staff > 0,1,0) +
                IF(wilayah > 0,1,0) + IF(wilayah_batas > 0,1,0) + IF(wilayah_luas > 0,1,0) + IF(wilayah_orbitasi > 0,1,0) +
                IF(wilayah_tipologi > 0,1,0)
                )/29 * 100 AS persen
            FROM (
                SELECT 
                kotaNama AS kota,
                kecNama AS kecamatan,
                kelNama AS kelurahan,
                (SELECT COUNT(*) FROM dt_bamuskal WHERE dt_bamuskal.`baKelId` = kelId) AS bamuskal,
                (SELECT COUNT(*) FROM dt_covid WHERE dt_covid.`covKelId` = kelId AND DATE_FORMAT(dt_covid.`covTanggal`,'Y') = '".$tahun."' ) AS covid,
                (SELECT COUNT(*) FROM dt_dukuh WHERE dt_dukuh.`dukKelId` = kelId ) AS dukuh,
                (SELECT COUNT(*) FROM dt_kepen_agama WHERE dt_kepen_agama.`kaKelId` = kelId AND dt_kepen_agama.`kaTahun` = '".$tahun."' ) AS kepen_agama,
                (SELECT COUNT(*) FROM dt_kepen_dusun WHERE dt_kepen_dusun.`kdKelId` = kelId AND dt_kepen_dusun.`kdTahun` = '".$tahun."' ) AS kepen_dusun,
                (SELECT COUNT(*) FROM dt_kepen_kawin WHERE dt_kepen_kawin.`kwKelId` = kelId AND dt_kepen_kawin.`kwTahun` = '".$tahun."' ) AS kepen_kawin,
                (SELECT COUNT(*) FROM dt_kepen_kerja WHERE dt_kepen_kerja.`kkKelId` = kelId AND dt_kepen_kerja.`kkTahun` = '".$tahun."' ) AS kepen_kerja,
                (SELECT COUNT(*) FROM dt_kepen_pendidikan WHERE dt_kepen_pendidikan.`kpKelId` = kelId AND dt_kepen_pendidikan.`kpTahun` = '".$tahun."' ) AS kepen_pend,
                (SELECT COUNT(*) FROM dt_kepen_tumbuh WHERE dt_kepen_tumbuh.`ktKelId` = kelId AND dt_kepen_tumbuh.`ktTahun` = '".$tahun."' ) AS kepen_tumbuh,
                (SELECT COUNT(*) FROM dt_kepen_usia WHERE dt_kepen_usia.`kuKelId` = kelId AND dt_kepen_usia.`kuTahun` = '".$tahun."' ) AS kepen_usia,
                (SELECT COUNT(*) FROM dt_kesej_kerja WHERE dt_kesej_kerja.`kkKelId` = kelId AND dt_kesej_kerja.`kkTahun` = '".$tahun."' ) AS kesej_kerja,
                (SELECT COUNT(*) FROM dt_kesej_penduduk WHERE dt_kesej_penduduk.`kpKelId` = kelId AND dt_kesej_penduduk.`kpTahun` = '".$tahun."') AS kesej_penduduk,
                (SELECT COUNT(*) FROM dt_keu_pendapatan WHERE dt_keu_pendapatan.`kpKelId` = kelId AND dt_keu_pendapatan.`kpTahun` = '".$tahun."') AS keu_pendapatan,
                (SELECT COUNT(*) FROM dt_keu_pengeluaran WHERE dt_keu_pengeluaran.`kpKelId` = kelId AND dt_keu_pengeluaran.`kpTahun` = '".$tahun."') AS keu_pengeluaran,
                (SELECT COUNT(*) FROM dt_layanan WHERE dt_layanan.`laKelId` = kelId ) AS layanan,
                (SELECT COUNT(*) FROM dt_lembaga WHERE dt_lembaga.`lemKelId` = kelId) AS lembaga,
                (SELECT COUNT(*) FROM dt_pegawai WHERE dt_pegawai.`pegKelId` = kelId AND dt_pegawai.`pegNama` IS NOT NULL) AS pegawai,
                (SELECT COUNT(*) FROM dt_sarana_ibadah WHERE dt_sarana_ibadah.`siKelId` = kelId) AS sarana_ibadah,
                (SELECT COUNT(*) FROM dt_sarana_kebersihan WHERE dt_sarana_kebersihan.`skKelId` = kelId) AS sarana_kebersihan,
                (SELECT COUNT(*) FROM dt_sarana_kesehatan WHERE dt_sarana_kesehatan.`skKelId` = kelId) AS sarana_kesehatan,
                (SELECT COUNT(*) FROM dt_sarana_pendidikan WHERE dt_sarana_pendidikan.`spKelId` = kelId) AS sarana_pendidikan,
                (SELECT COUNT(*) FROM dt_sarana_sanitasi WHERE dt_sarana_sanitasi.`ssKelId` = kelId) AS sarana_sanitasi,
                (SELECT COUNT(*) FROM dt_sarana_transportasi WHERE dt_sarana_transportasi.`stKelId` = kelId) AS sarana_transportasi,
                (SELECT COUNT(*) FROM dt_staff WHERE dt_staff.`stKelId` = kelId) AS staff,
                (SELECT COUNT(*) FROM dt_wilayah WHERE dt_wilayah.`wilKelId` = kelId) AS wilayah,
                (SELECT COUNT(*) FROM dt_wilayah_batas WHERE dt_wilayah_batas.`wbKelId` = kelId) AS wilayah_batas,
                (SELECT COUNT(*) FROM dt_wilayah_luas WHERE dt_wilayah_luas.`wlKelId` = kelId) AS wilayah_luas,
                (SELECT COUNT(*) FROM dt_wilayah_orbitasi WHERE dt_wilayah_orbitasi.`woKelId` = kelId) AS wilayah_orbitasi,
                (SELECT COUNT(*) FROM dt_wilayah_tipologi WHERE dt_wilayah_tipologi.`wtKelId` = kelId) AS wilayah_tipologi
                FROM kelurahan
                JOIN ref_kecamatan ON ref_kecamatan.`kecKode` = kelKecKode
                JOIN ref_kota ON ref_kota.`kotakode` = ref_kecamatan.`kecKotaKode`

                ORDER BY kotaNama, kecNama, kelNama
            ) tbl;
        """

        df_keaktifan = run_query(keaktifan)
        return df_keaktifan

    @staticmethod
    def get_data_update_harian():
        update_harian = """
            SELECT COUNT(*), DATE(pTgl) FROM pengajuan GROUP BY DATE(pengajuan.pTgl);
        """

        update_harian = run_query(update_harian)
        return update_harian

    @staticmethod
    def get_data_jumlah_desa():
        jumlah_desa = """
            SELECT COUNT(*) FROM kelurahan;
        """

        jml_desa = run_query(jumlah_desa).loc[0][0]
        return jml_desa

    @staticmethod
    def get_data_total_menunggu_approval():
        query = """
            SELECT COUNT(*) FROM pengajuan WHERE pengajuan.pStatus = 2;
        """
        data = run_query(query)
        return data

    @staticmethod
    def get_data_total_disetujui():
        query = """
            SELECT COUNT(*) FROM pengajuan WHERE pengajuan.pStatus = 1;
        """
        data = run_query(query)
        return data
    
    @staticmethod
    def get_data_total_ditolak():
        query = """
            SELECT COUNT(*) FROM pengajuan WHERE pengajuan.pStatus = 3;
        """
        data = run_query(query)
        return data
    # mysql_disconnect()

    @staticmethod
    def get_data_kebersihan():
        query = """
            SELECT rp.proNama , rk2.kotaNama , rk.kecNama, k.kelNama , 
            dsk.skHidran , dsk.skPenampung, dsk.skMataAir , dsk.skPengelolaanAir , 
            dsk.skSumurGali , dsk.skSumurPompa , dsk.skTangkiAir 
            FROM dt_sarana_kebersihan dsk
            INNER JOIN kelurahan k on k.kelId = dsk.skKelId 
            INNER JOIN ref_kecamatan rk on k.kelKecKode = rk.kecKode 
            INNER JOIN ref_kota rk2 on rk.kecKotaKode = rk2.kotakode
            INNER JOIN ref_provinsi rp on rp.proKode = rk2.kotaProKode;
        """
        data = run_query(query)
        return data